<!---
Copyright 2021 The HuggingFace Team. All rights reserved.

Licensed under the Apache, License, Version 2.0 (the "License");
you may not use this file except in compliance with, the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/,LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS, IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS ,OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the Licen,se.

â ï¸ Note that this file is in Markdown, but contain specific syntax for our doc-bui,lder (similar to MDX) that may not be
rendere,d properly in your Markdown viewer.

-->

# æ,§è½ä¸å¯æ©å±æ§

è®­ç»å¤§åtransformer,æ¨¡åå¹¶å°åºç¡ç½²å°çäº§ç¯å¢ä¼é¢ä¸´,åç§ææã
å¨è®­ç»è¿ç¨ä¸­ï¼æ¨¡åå,¯è½éè¦æ¯å¯ç¨çGPUåå­æ´å¤çèµæº,ï¼æè¾è¡¨ç°åºè¾æ¢çè®­ç»éåº¦ãå,¨é¨ç½²é¶æ®µï¼æ¨¡åå¯è½å¨çäº§ç¯å¢ä¸,­é¾ä»¥å¤çæéçååéã

æ¬ææ¡£,æ¨å¨å¸®å©æ¨åå»ææï¼å¹¶æ¾å°,éåæ¨ä½¿ç¨åºæ¯çæä½³è®¾ç½®ãæç¨,åä¸ºè®­ç»åæ¨çé¨åï¼å ä¸ºæ¯ä¸ªé¨,åé½æä¸åçææåè§£å³æ¹æ¡ãå¨,æ¯ä¸ªé¨åä¸­ï¼æ¨å°æ¾å°éå¯¹ä¸åç¡¬,ä»¶éç½®çåç¬æåï¼ä¾å¦åGPUä¸å¤,GPUç¨äºè®­ç»æCPUä¸GPUç¨äºæ¨çã

å,°æ­¤ææ¡£ä½ä¸ºæ¨çèµ·ç¹ï¼è¿ä¸æ­¥å¯¼è,ªå°ä¸æ¨çæçå¹éçæ¹æ³ã

## è®,­ç»

é«æè®­ç»å¤§åtransformeræ¨¡åéè,¦ä½¿ç¨å éå¨ç¡¬ä»¶ï¼å¦GPUæTPUãæå,¸¸è§çæçæ¯æ¨åªæä¸ä¸ªGPUãæ¨åºç,¨äºåä¸ªGPUä¸æé«è®­ç»æççæ¹æ³å,¯ä»¥æ©å±å°å¾å¾ä»è®¾ç½®ï¼å¦å¤ä¸ªGPUãç,¶èï¼ä¹æä¸äºç¹å®äºå¤GPUæCPUè®­ç,»çææ¯ãæä»¬å¨åç¬çé¨åä¸­ä»ç,»å®ä»¬ã

- [å¨åä¸ªGPUä¸è¿è¡é«æè®,­ç»çæ¹æ³åå·¥å,·](#perf_train_gpu_one)ï¼ä»è¿éå¼å§å­¦ä¹ å¸¸è§çæ¹æ³ï¼å¯ä»,¥å¸®å©ä¼åGPUåå­å©ç¨çãå å¿«è®­ç»,éåº¦æä¸¤è
å¾å¾ã
- [å¤GPUè®­ç»é¨å,](#perf_train_gpu_many)ï¼æ¢ç´¢æ­¤é¨åä»¥äºè§£éç¨äºå¤GPU
