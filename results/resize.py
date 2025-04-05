import os
from PIL import Image

def resize_images_to_aspect_ratio(input_folder, output_folder, target_aspect_ratio=(8, 5)):
    """
    调整文件夹中所有图片的长宽比为目标比例（如 8:5），并保存到输出文件夹。
    
    参数：
    - input_folder: 输入图片文件夹路径
    - output_folder: 输出图片文件夹路径
    - target_aspect_ratio: 目标长宽比，默认为 (8, 5)
    """
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # 检查是否为图片文件
        if not os.path.isfile(file_path) or filename.lower().split('.')[-1] not in ['jpg', 'jpeg', 'png', 'bmp']:
            continue
        
        try:
            # 打开图片
            with Image.open(file_path) as img:
                original_width, original_height = img.size
                
                # 计算目标尺寸
                target_width, target_height = calculate_target_size(original_width, original_height, target_aspect_ratio)
                
                # 调整图片尺寸
                resized_img = img.resize((target_width, target_height), Image.ANTIALIAS)
                
                # 保存调整后的图片
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path, format=img.format)
                print(f"已调整并保存：{output_path}")
        
        except Exception as e:
            print(f"处理图片 {filename} 时出错：{e}")

def calculate_target_size(original_width, original_height, target_aspect_ratio):
    """
    根据目标长宽比计算调整后的图片尺寸。
    
    参数：
    - original_width: 原始宽度
    - original_height: 原始高度
    - target_aspect_ratio: 目标长宽比 (width, height)
    
    返回：
    - 调整后的宽度和高度
    """
    target_width_ratio, target_height_ratio = target_aspect_ratio
    original_aspect_ratio = original_width / original_height
    
    if original_aspect_ratio > (target_width_ratio / target_height_ratio):
        # 图片过宽，按高度调整
        new_height = original_height
        new_width = int(new_height * (target_width_ratio / target_height_ratio))
    else:
        # 图片过高，按宽度调整
        new_width = original_width
        new_height = int(new_width * (target_height_ratio / target_width_ratio))
    
    return new_width, new_height

# 示例调用
input_folder = "results/after"  # 替换为你的输入文件夹路径
output_folder = "results/after"  # 替换为你的输出文件夹路径
resize_images_to_aspect_ratio(input_folder, output_folder)