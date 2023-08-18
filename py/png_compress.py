import subprocess
import os

def compress_png(input_path, output_path, target_size_kb):

    file_exec=input_path
    while True:
        try:
            # 调用 pngquant 命令行工具进行压缩
            print(file_exec)
            result=subprocess.run(["pngquant", '--force', '--output', output_path, '--quality', '20', '--speed', '11', "--", file_exec], check=True)
            if result.returncode == 0:
                size=os.path.getsize(output_path)
                if size > target_size_kb * 1024:
                    file_exec=output_path
                    continue
                else:
                    break
        except subprocess.CalledProcessError as e:
            print("压缩过程中出现错误:", e)
            