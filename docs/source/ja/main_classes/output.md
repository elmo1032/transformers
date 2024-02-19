<!-- Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# Model outputs

All models have outputs of the form [`~util.ModelOutput`], which are dictionaries containing various information about 
the model's output. These dictionaries can contain model-specific keys, but they all share the following base keys:

- `loss`: The loss associated with the model's output. This is only present if the model is being trained or if the 
`output_attentions` argument is set to `True`.
- `logits`: The raw, unnormalized scores for each class in the model's output.

Here is an example of how to use a model and access its outputs:




In this example, `outputs` is an instance of [`~modeling_outputs.SequenceClassifierOutput`], which has the following keys:

- `loss`: The loss associated with the model's output. This is only present if the model is being trained or if the 
`output_attentions` argument is set to `True`.
- `logits`: The raw, unnormalized scores for each class in the model's output.
- `hidden_states`: The hidden states for each layer in the model. This is only present if the `output_hidden_states` 
argument is set to `True`.
- `attentions`: The attention weights for each layer in the model. This is only present if the `output_attentions` 
argument is set to `True`.

In this example, `outputs.loss` will be `None` because the model is not being trained and `outputs.attentions` will 
also be `None` because the `output_attentions` argument was not set to `True`.

You can access the values of these keys using dictionary syntax, like so:




If you want to access only the first few keys of the dictionary, you can use slicing:




This will return a new dictionary containing only the `loss` and `logits` keys.

You can also convert the dictionary to a tuple using the `to_tuple` method:




This will return a tuple containing the values of the `loss`, `logits`, `hidden_states`, and `attentions` keys, in that 
order.

Here is a list of all the possible model output classes:

- [`~utils.ModelOutput`]
- [`~modeling_outputs.BaseModelOutput`]
- [`~modeling_outputs.BaseModelOutputWithPooling`]
- [`~modeling_outputs.BaseModelOutputWithCrossAttentions`]
- [`~modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions`]
- [`~modeling_outputs.BaseModelOutputWithPast`]
- [`~modeling_outputs.BaseModelOutputWithPastAndCrossAttentions`]
- [`~modeling_outputs.Seq2SeqModelOutput`]
- [`~modeling_outputs.CausalLMOutput`]
- [`~modeling_outputs.CausalLMOutputWithCrossAttentions`]
- [`~modeling_outputs.CausalLMOutputWithPast`]
- [`~modeling_outputs.MaskedLMOutput`]
- [`~modeling_outputs.Seq2SeqLMOutput`]
- [`~modeling_outputs.NextSentencePredictorOutput`]
- [`~modeling_outputs.SequenceClassifierOutput`]
- [`~modeling_outputs.Seq2SeqSequenceClassifierOutput`]
- [`~modeling_outputs.MultipleChoiceModelOutput`]
- [`~modeling_outputs.TokenClassifierOutput`]
- [`~modeling_outputs.QuestionAnsweringModelOutput`]
- [`~modeling_outputs.Seq2SeqQuestionAnsweringModelOutput`]
- [`~modeling_outputs.Seq2SeqSpectrogramOutput`]
- [`~modeling_outputs.SemanticSegmenterOutput`]
- [`~modeling_outputs.ImageClassifierOutput`]
- [`~modeling_outputs.ImageClassifierOutputWithNoAttention`]
- [`~modeling_outputs.DepthEstimatorOutput`]
- [`~modeling_outputs.Wav2Vec2BaseModelOutput`]
- [`~modeling_outputs.XVectorOutput`]
- [`~modeling_outputs.Seq2SeqTSModelOutput`]
- [`~modeling_outputs.Seq2SeqTSPredictionOutput`]
- [`~modeling_outputs.SampleTSPredictionOutput`]
- [`~modeling_tf_outputs.TFBaseModelOutput`]
- [`~modeling_tf_outputs.TFBaseModelOutputWithPooling`]
- [`~modeling_tf_outputs.TFBaseModelOutputWithPoolingAndCrossAttentions`]
- [`~modeling
