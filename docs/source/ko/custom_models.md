<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# ì¬ì©ì, ì ì ëª¨ë¸ ê³µì íê¸°[[sharing-custom,-models]]

🤗 Transformers ë¼ì´ë¸ë¬ë¦¬ë, ì½ê² íì¥í  ì ìëë¡ ì¤ê³ëì,ìµëë¤. 
ëª¨ë  ëª¨ë¸ì ì¶ìí ìì,´ ì ì¥ìì ì§ì ë íì í´ëì ì,ì í ì½ë©ëì´ ìì¼ë¯ë¡, ìì½ê² ë,ª¨ë¸ë§ íì¼ì ë³µì¬íê³  íìì ë°,ë¼ ì¡°ì í  ì ììµëë¤.

ìì í ì,ë¡ì´ ëª¨ë¸ì ë§ëë ê²½ì°ìë ì²ì,ë¶í° ììíë ê²ì´ ë ì¬ì¸ ì ì,ìµëë¤.
ì´ íí ë¦¬ì¼ììë Transf,ormers ë´ìì ì¬ì©í  ì ìëë¡ ì¬ì,©ì ì ì ëª¨ë¸ê³¼ êµ¬ì±ì ìì±íë, ë°©ë²ê³¼ 
🤗 Transformers ë¼ì´ë¸ë¬ë¦¬,ì ìë ê²½ì°ìë ëêµ¬ë ì¬ì©í  ì, ìëë¡ (ìì¡´ì±ê³¼ í¨ê») ì»¤ë®¤ëí,°ì ê³µì íë ë°©ë²ì ë°°ì¸ ì ìì,µëë¤.

[timm ë¼ì´ë¸ë¬ë¦¬](https://gith,ub.com/rwightman/pytorch-image-models)ì Res,Net í´ëì¤ë¥¼ [`PreTrainedModel`]ë¡ ëí,í ResNet ëª¨ë¸ì ìë¡ ëª¨ë  ê²ì ì,¤ëª Klein,í©ëë¤.

## ì¬ì©ì ì ì êµ¬ì± ì,ì±íê¸°[[writing-a-custom-configuration]]
,
ëª¨ë¸ì ë¤ì´ê°ê¸° ì ì ë¨¼ì  êµ¬ì±ì, ìì±í´ë³´ëë¡ íê² ìµëë¤.
ëª¨ë¸,ì `configuration`ì ëª¨ë  ì¤ìí ê²ë¤ì í¬,í¨íê³  ìë ê°ì²´ìëë¤.
ë¤ì ì¹ì,ìì ë³¼ ì ìë¯ì´, ëª¨ë¸ì `config,`ë¥¼ ì¬ì©í´ìë§ ì´ê¸°íí  ì ìê¸° ,ëë¬¸ì ìë²½í êµ¬ì±ì´ íìí©ëë¤,.

ìë ììììë ResNet í´ëì¤ì, ì¸ì(argument)ë¥¼ ì¡°ì í´ë³´ê² ì
