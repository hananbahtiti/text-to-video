import logging
from tasks import task_model_flux_pro, task_model_flux_pro_ultra, task_model_flux_dev, task_model_ideogram_v2, task_model_flux_schnell  # Add all models here

def run_model_task(**kwargs):
    model_name = kwargs.get("model_name")
    
    if model_name == "fal-ai/luma-dream-machine/ray-2":
        task_model_luma_dream_machine_ray_2.generate_image(**kwargs)
    elif model_name == "fal-ai/luma-dream-machine":
        task_model_luma_dream_machine.generate_image(**kwargs)
    elif model_name == "fal-ai/kling-video/v1.6/standard/text-to-video":
        task_model_kling_video_v1_6.generate_image(**kwargs)
    elif model_name == "fal-ai/cogvideox-5b":
        task_model_cogvideox_https://fal.ai/models/fal-ai/hunyuan-video5b.generate_image(**kwargs)
    elif model_name == "fal-ai/hunyuan-video":
        task_model_hunyuan_video.generate_image(**kwargs)
    else:
        logging.error(f"Unsupported model: {model_name}")
        raise ValueError(f"Unsupported model: {model_name}")
