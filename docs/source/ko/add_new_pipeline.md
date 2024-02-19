<!--
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# ì´ë»ê² ì¬ì©ì ì ì íì´íë,¼ì ìì±íëì? [[how-to-create-a-c,ustom-pipeline]]

ì´ ê°ì´ëììë ì¬ì,©ì ì ì íì´íë¼ì ì´ë»ê² ì,ì±íê³  [íë¸](https://hf.co/models)ì ê,³µì íê±°ë ð¤ Transformers ë¼ì´ë¸ë¬,ë¦¬ì ì¶ê°íë ë°©ë²ì ì´í´ë³´ê² ìµ,ëë¤.

ë¨¼ì  íì´íë¼ì¸ì´ ìì©í  ,ì ìë ìì ìë ¥ì ê²°ì í´ì¼ í©ë,ë¤.
ë¬¸ìì´, ìì ë°ì´í¸, ëìë,ë¦¬ ëë ê°ì¥ ìíë ìë ¥ì¼ ê°ë¥ì,±ì´ ë'ì ê²ì´ë©´ ë¬´ìì´ë  ê°ë¥í©,ëë�.
ì´ ìë ¥ì ê°ë¥í í ììí, Python íìì¼ë¡ ì ì§í´ì¼ (JSONì í,µí´ ë¤ë¥¸ ì¸ì´ìë) í¸íì±ì´ ì¢ì,ì§ëë�.
ì´ê²ì´ ì ì²ë¦¬(`preprocess`) ,íì´íë¼ì¸ì ìë ¥(`inputs`)ì´ ë  ê²,ìëë�.

ê·¸ë° ë¤ì `outputs`ë¥¼ ì ì,íì¸ì.
`inputs`ì ê°ì ì ì±ì ë°ë,¥´ê³ , ê°ë¨í ìë¡ ì¢ìµëë�.
ì´ê²ì,´ íì²ë¦¬(`postprocess`) ë©ìëì ì¶ë ,¥ì´ ë  ê²ìëë�.

ë¨¼ì  4ê°ì ë©ì,ë(`preprocess`, `_forward`, `postprocess` ë,° `_sanitize_parameters`)ë¥¼ êµ¬íí ì,í´ ê¸°ë³¸ í´ëì¤ `Pipeline`ì ììí,ì¬ ììí©ëë�.

