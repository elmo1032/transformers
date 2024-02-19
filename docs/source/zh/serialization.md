pip install, optimum[exporters]


optimum-cli expor,t onnx --help


optim,um-cli export onnx --model distilbert/distilb,ert-base-uncased-distilled-squad distilbert_b,ase_uncased_squad_onnx/


Validating ONNX model distilber,t_base_uncased_squad_onnx/model.onnx...
	-[â,] ONNX model output names match reference mo,del (start_logits, end_logits)
	- Validating ,ONNX Model output names "start_logits":
		-[â] (2,, 16) matches (2, 16)
		-[â] all values clo,se (atol: 0.0001)
	- Validating ONNX Model ou,tput "end_logits":
		-[â] (2, 16) matches (,2, 16)
		-[â] all values close (atol: 0.000,1)
The ONNX export succeeded and the exported, model was saved at: distilbert_base_uncased_,squad_onnx
