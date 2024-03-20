
import cv2
import gradio as gr
from gradio_point_promptable_image import PointPromptableImage

BLUE = (135, 206, 235)
PINK = (239, 149, 186)

image_examples = [{"image": "images/cat.png", "points": []}]

def get_point_inputs(prompts):
    point_inputs = []
    for prompt in prompts:
        if prompt[5] == 4.0:
            point_inputs.append((prompt[0], prompt[1], prompt[2]))

    return point_inputs

def process_input(input_dict):
    img, points = input_dict['image'], input_dict['points']

    point_inputs = get_point_inputs(points)

    for point in point_inputs:
        x, y = int(point[0]), int(point[1])
        cv2.circle(img, (x, y), 2, (0, 0, 0), thickness=10)
        if point[2] == 1:
            cv2.circle(img, (x, y), 2, BLUE, thickness=8)
        else:
            cv2.circle(img, (x, y), 2, PINK, thickness=8)

    return img

demo = gr.Interface(
    process_input,
    PointPromptableImage(),
    gr.Image(),
    examples=image_examples,
)

if __name__ == "__main__":
    demo.launch()
