import glob
import json

from langchain_core.output_parsers.json import parse_json_markdown

from ai_ocr.azure.doc_intelligence import get_ocr_results
from ai_ocr.azure.openai_ops import load_image, get_size_of_base64_images
from ai_ocr.chains import get_structured_data
from ai_ocr.model import Config


def process_pdf(file_to_ocr: str, prompt: str, json_schema: str, config: Config = Config()) -> any:
    ocr_result = get_ocr_results(file_to_ocr)
    pdf_path = file_to_ocr.replace(file_to_ocr.split("\\")[-1], "")
    imgs = glob.glob(f"{pdf_path}\\page*.png")
    # limit imgs by default
    imgs = imgs[:config.max_images]
    imgs = list(map(lambda x: load_image(x), imgs))
    # Check if images total size over 20MB
    total_size = get_size_of_base64_images(imgs)
    # Reduce image sizes if total size is over 20MB
    max_size = config.gpt_vision_limit_mb * 1024 * 1024  # 20MB
    sizes = [2, 1, 0]  # sizes to reduce to
    for size in sizes:
        imgs = imgs[:size]
        total_size = get_size_of_base64_images(imgs)
        if total_size <= max_size:
            break
    structured = get_structured_data(ocr_result.content, prompt, json_schema, imgs)
    x = parse_json_markdown(structured.content)
    return json.dumps(x)
