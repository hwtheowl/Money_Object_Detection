import os

# 스마트폰에서 재생 가능하도록 코덱 변환
def convert_codec(source_path, output_path):
    temp_path = output_path + '.temp.mp4'
    os.system(f"ffmpeg -i {source_path} -vcodec libx264 {temp_path}")
    os.rename(temp_path, output_path)

# 모델 동작 함수
def detecte(source_folder, result_folder, conf=0.25, convert=1):
    detect_py = "/home/hwl/Workspace/yolov5/detect.py"
    weights = "/home/hwl/Workspace/Money_Object_Detection/best.pt"

    os.system(f"python {detect_py} --weights {weights} --img 640 --conf {conf} --source {source_folder} --project {result_folder}")

    # 변환 여부 선택
    if convert == 1:
        # 결과 하위 폴더 목록 만들기(코덱 변경 위해)
        folders = [f for f in os.listdir(result_folder) if f.startswith('exp')]
        folders.sort()
        
        if len(folders) > 0:
            latest_exp_folder = folders[-1]
            result_subfolder = os.path.join(result_folder, latest_exp_folder)

            for filename in os.listdir(result_subfolder):
                if filename.endswith('.mp4'):
                    result_file = os.path.join(result_subfolder, filename)
                    convert_codec(result_file, result_file)

# 경로 지정
result_folder = "/home/hwl/Workspace/Money_Object_Detection/results"
source_folder = "/home/hwl/Workspace/Money_Object_Detection/test_data/"

# 모델 동작
detecte(source_folder, result_folder, conf=0.45, convert=0)