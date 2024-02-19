<!--
Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# ð¤ Accelerateë¥¼ íì©í ë¶ì° íìµ[[distribu,ted-training-with-accelerate]]

ëª¨ë¸ì´ ì»¤,ì§ë©´ì ë³ë ¬ ì²ë¦¬ë ì íë íëì,¨ì´ìì ë í° ëª¨ë¸ì íë ¨íê³  í,ë ¨ ìëë¥¼ ëª ë°°ë¡ ê°ìííê¸° ìí, ì ëµì¼ë¡ ë±ì¥íìµëë¤. Hugging F,aceììë ì¬ì©ìê° íëì ë¨¸ì ì, ì¬ë¬ ê°ì GPUë¥¼ ì¬ì©íë  ì¬ë¬ ë¨¸,ì ì ì¬ë¬ ê°ì GPUë¥¼ ì¬ì©íë  ëª¨ë,  ì íì ë¶ì° ì¤ì ìì ð¤ Transfo,rmers ëª¨ë¸ì ì½ê² íë ¨í  ì ìëë¡, ëê¸° ìí´ [ð¤ Accelerate](https://hug,gingface.co/docs/accelerate) ë¼ì´ë¸ë¬ë¦¬ë,¥¼ ë§ë¤ììµëë¤. ì´ íí ë¦¬ì¼ìì,ë ë¶ì° íê²½ìì íë ¨í  ì ìëë,¡ ê¸°ë³¸ PyTorch íë ¨ ë£¨íë¥¼ ì»¤ì¤í°ë,§ì´ì¦íë ë°©ë²ì ììë´ìë¤.

##, ì¤ì [[setup]]

ð¤ Accelerate ì¤ì¹ ìì,íê¸°:




ê·¸ ë¤ì, [`~accelerate.Accelerator`] ê°,ì²´ë¥¼ ë¶ë¬ì¤ê³  ìì±í©ëë¤. [`~accelerate.Accelerator`]ë ìëì¼ë¡ ë¶ì° ì,¤ì  ì íì ê°ì§íê³  íë ¨ì íìí, ëª¨ë  êµ¬ì± ììë¥¼ ì´ê¸°íí©ëë¤,. ì¥ì¹ì ëª¨ë¸ì ëªëì ì¼ë¡ ë°°ì¹í,  íìë ììµëë¤.




## ê°ìíë¥¼ ìí ì,¤ë¹[[prepare-to-accelerate]]

ë¤ì ë¨ê³,ë ê´ë ¨ë ëª¨ë  íë ¨ ê°ì²´ë¥¼ [`~acce,lerate.Accelerator.prepare`] ë©ìëì ì ,ë¬íë ê²ìëë¤. ì¬ê¸°ìë íë ¨ ë,° íê° ë°ì´í°ë¡ë, ëª¨ë¸ ë° ìµí°ë,§ì´ì ê° í¬í¨ë©ëë¤:

