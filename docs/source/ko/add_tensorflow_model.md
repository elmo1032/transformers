<!-- Copyright 2022 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# ð¤ Transformers ëª¨ë¸ì, TensorFlowë¡ ë³ííëì? [[how-to-conv,ert-a-transformers-model-to-tensorflow]]

ð¤, Transformersììì²ë¼ ì¬ì©í  ì ìë, ì¬ë¬ ê°ì§ íë ììí¬ê° ìë¤ë, ê²ì ì íë¦¬ì¼ì´ì ì¤ê³í  ë ê,·¸ë¤ì ê°ì ì ì ì°íê² ì´ì©í  ì, ìë¤ë ì¥ì ì´ ìì§ë§, ëª¨ë¸ ë³ë¡, í¸íì±ì ì¶ê°í´ì¼ íë¤ë ê²ì´ ì ì°ë¡ ì¸ë¯¸í©ëë¤. ì¢ì ììì ê¸°ì¡´ ëª¨ë¸ì TensorFlow, í¸íì±ì ì¶ê°íë ê²ìëë¤! 

ë§ì½ ëê·ëª¨ TensorFlow ëª¨ë¸ì ,ë ê¹ì´ ì´í´íë ¤ê±°ë, ì¤í ìì¤ì, í° ê¸°ì¬ë¥¼ íë ¤ê±°ë, ì íí ëª¨ë,¸ì Tensorflowë¥¼ íì©íë ¤íë¤ë©´, ì,´ ìë´ìë ì¬ë¬ë¶ê» ëìì´ ë  ê²,ìëë¤.

ì´ ê°ì´ëë Hugging Face í,ì ìµìíì ê°ë ìëìì ð¤ Tra,nsformersìì ì¬ì©ëë TensorFlow ëª¨ë,¸ ê°ì¤ì¹ì/ëë ìí¤í,ì²ë¥¼ ê¸°ì¬í,  ì ìë ì»¤ë®¤ëí° êµ¬ì±ìì¸ ì¬ë¬ë¶ì ëìì¼ë¡ í©ëë¤. 
ìë¡ì´ ëª,¨ë¸ì ìì±íë ê²ì ì¬ì´ ì¼ì´ ì,ëì§ë§, ì´ ê°ì´ëë¥¼ íµí´ ì¡°ê¸ ë, íë¤ê³  í¨ì¬ ì¬ì´ ììì¼ë¡ ë§ë¤ ,ì ììµëë¤. 
ëª¨ëì ê²½íì ëª¨ì¼,ë ê²ì ì´ ììì ì ì°¨ì ì¼ë¡ ë ,ì½ê² ë§ëë ë° êµì¥í ì¤ìíê¸° ë,ë¬¸ì, ì´ ê°ì´ëë¥¼ ê°ì ìí¬ë§í, ì ìì´ ë ì¤ë¥´ë©´ ê³µì íìëê±¸ ì ,ê·¹ì ì¼ë¡ ê¶ì¥í©ëë¤!

ë ê¹ì´ ì,ìë³´ê¸° ì ì, ð¤ Transformers
