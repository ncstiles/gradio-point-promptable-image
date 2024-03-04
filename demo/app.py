
import gradio as gr
from gradio_point_promptable_image import PointPromptableImage
import cv2

PURPLE = (177, 157, 217)

image_examples = [{"image": "images/cat.png", "points": []}]

def get_point_inputs(prompts):
    point_inputs = []
    for prompt in prompts:
        if prompt[2] == 1.0 and prompt[5] == 4.0:
            point_inputs.append((prompt[0], prompt[1]))

    return point_inputs

def process_input(input_dict):
    img, points = input_dict['image'], input_dict['points']

    point_inputs = get_point_inputs(points)

    for point in point_inputs:
        x, y = int(point[0]), int(point[1])
        cv2.circle(img, (x, y), 2, PURPLE, thickness=10)

    return img

demo = gr.Interface(
    process_input,
    PointPromptableImage(),
    gr.Image(),
    examples=image_examples,
)

if __name__ == "__main__":
    demo.launch()
