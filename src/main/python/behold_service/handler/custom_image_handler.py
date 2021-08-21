
import torch
import logging
import time
from ts.torch_handler.image_classifier import ImageClassifier
from torchvision import transforms

class CustomImageHandler(ImageClassifier):

    # transforms taken from ImageClassifier with ColorJitter and Pad added
    image_processing = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.2),
        transforms.Pad(2),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])


    def inference(self, data, *args, **kwargs):
        """
        The Inference Function is used to make a prediction call on the given input request.
        The user needs to override the inference function to customize it.

        Args:
            data (Torch Tensor): A Torch Tensor is passed to make the Inference Request.
            The shape should match the model input shape.

        Returns:
            Torch Tensor : The Predicted Torch Tensor is returned in this function.
        """

        #below is taken from BaseHandler with logging added
        inference_start = time.time()
        marshalled_data = data.to(self.device)
        with torch.no_grad():
            results = self.model(marshalled_data, *args, **kwargs)

        postprocess_start = time.time()
        logging.info("some custom logging!")
        logging.info("inference time: %.2f", (postprocess_start - inference_start) * 1000)
        return results

    def postprocess(self, data):
        results = super().postprocess(data)

        logging.info("here be some results")
        logging.info(results)
        top_three_results = get_top_three_results(results)
        output_results_to_logs(top_three_results)

        return results

    def handle(self, data, context):
        # need to do some funky stuff here if balloon predicted
        first_output = super().handle(data, context)

        # check if balloon predicted if so need to pass different model
        logging.info(first_output)

        # guess we need to reinitialize
        # model_file = self.manifest["model"].get("modelFile", "")
        logging.info(type(context.manifest))
        logging.info(context.manifest)
        #change the context to new model
        context.manifest["model"]["modelFile"] = "model.py"
        super().initialize(context)
        second_output = super().handle(data, context)

        return first_output

#TODO split into separate file and add tests?
def get_top_three_results(results):
    #results is list, first item contains a dict
    predictions_dict = results[0]
    predictions_classes_list = list(predictions_dict.keys())
    return predictions_classes_list[0:3]

def output_results_to_logs(results_to_log):
    for result_to_log in results_to_log:
        logging.info(result_to_log)