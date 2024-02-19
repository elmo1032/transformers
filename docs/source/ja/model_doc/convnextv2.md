





You can also train a new ConvNeXt V2 model from scratch using the `ConvNeXtV2Model` class. This allows you to customize the model's architecture and training procedure to suit your specific needs.

## Resources

For more information about using the ConvNeXt V2 model, please see the following resources:

- [ConvNeXt V2 model card](https://huggingface.co/facebook/convnext-v2-base)
- [ConvNeXt V2 example notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/convnext_v2.ipynb)
- [ConvNeXt V2 model documentation](https://huggingface.co/docs/transformers/model_doc/convnextv2)

## Model Config

[[autodoc]] ConvNextV2Config

## Model

[[autodoc]] ConvNextV2Model
    - forward

## Image Classification

[[autodoc]] ConvNextV2ForImageClassification
    - forward

## TensorFlow Model

[[autodoc]] TFConvNextV2Model
    - call

## TensorFlow Image Classification

[[autodoc]] TFCo
