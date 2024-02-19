<!--Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# å¾®è°é¢è®­ç»æ¨¡å

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/transformers/blob/main/examples/pytorch/text-classification/run_glue.py)

ä½¿ç¨é¢è®­ç»æ¨¡åæè®¸å¤æ¾èçå¥½å¤ãå®éä½äºè®¡ç®ææ¬ï¼åå°äºç¢³ææ¾ï¼åæ,¶å è½½æå¾®è°çæ¨¡åï¼èæ éä»å¤´å¼å§è®­ç»ä¸ä¸ªãð¤ Transformers æä¾äºæ¶ååç§ä»»å¡ç¸å¾ązçé¢è®­ç»æ¨¡åãå½æ¨ä½¿ç¨é¢è®­ç»æ¨¡åæ¶ï¼æ¨éè¦å¨ä¸ä»»å¡ç¸å¾ązçæ°æ®éä¸è®­ç»è¯¥æ¨¡åãè¿ç§æä½è¢«ç§°ä¸ºå,¾®è°ï¼æ¯ä¸ç§éå¸¸å¼ºå¤§çè®­ç»ææ¯ã,å¨æ¬æç¨ä¸­ï¼æ¨å°ä½¿ç¨æ¨éæ©çæ,·±åº¦å­¦ä¹ æ¡æ¶æ¥å¾®è°ä¸ä¸ªé¢è®­ç»æ¨¡å,ï¼

* ä½¿ç¨ ð¤ Transformers ç [`Trainer`] æ¥å¾®è°é¢è®­ç»æ¨¡åã
* å¨ Tensor,Flow ä¸­ä½¿ç¨ Keras æ¥å¾®è°é¢è®­ç»æ¨¡å,ã
* å¨åç PyTorch ä¸­å¾®è°é¢è®­ç»æ¨¡,åã

<a id='data-processing'></a>

## åå,¤æ°æ®é

<Youtube id="_BZearw7f0w"/>

å¨,æ¨è¿è¡é¢è®­ç»æ¨¡åå¾®è°ä¹åï¼éè¦,ä¸è½½ä¸ä¸ªæ°æ®éå¹¶ä¸ºè®­ç»åå¥½åå¤,ãä¹åçæç¨åæ¨å±ç¤ºäºå¦ä½å¤ç,è®­ç»æ°æ®ï¼ç°å¨æ¨ææºä¼å°è¿äºæ,è½ä»è¯¸å®è·µï¼

é¦å¾ï¼å è½½[Yelpè¯è®,º](https://huggingface.co/datasets/yelp_revie,w_full)æ°æ®éï¼

