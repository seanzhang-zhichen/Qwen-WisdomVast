<p align="left">
    <a href="README_CN.md">中文</a>&nbsp ｜ &nbspEnglish
</p>
<br><br>

<p align="center">
<a href='https://huggingface.co/spaces/zhichen'>
<img src='./images/logo.png'>
</a>
</p>

<div align="center">
  <p align="center">
    <h3> Qwen-WisdomVast (千问-智瀚)</h3>

<p align="center">
      <a href='https://huggingface.co/zhichen'>
        <img src='https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Qwen%20WisdomVast-yellow'>
      </a>
      <a href='https://modelscope.cn/profile/seanzhang'>
        <img src='https://img.shields.io/badge/🤖 ModelScope-Qwen%20WisdomVast-blue'>
      </a>
      <br>
      <a href=href="https://github.com/seanzhang-zhichen/Qwen-WisdomVast/stargazers">
        <img src="https://img.shields.io/github/stars/seanzhang-zhichen/Qwen-WisdomVast?color=ccf">
      </a>
      <a href="https://github.com/seanzhang-zhichen/Qwen-WisdomVast/blob/main/LICENSE">
        <img alt="GitHub Contributors" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" />
      </a>
</p>
</div>


## Introduce

**Qwen-WisdomVast** is a large model trained on 1 million high-quality Chinese multi-turn SFT data, 200,000 English multi-turn SFT data, and 2,000 single-turn self-cognition data, using the training methods of [DORA](https://arxiv.org/pdf/2402.09353.pdf) and [LORA+](https://arxiv.org/pdf/2402.12354.pdf) based on **Qwen1.5-7B** as the base. Compared to Qwen1.5-7B-Chat, it has improved **mathematical abilities** by **5.16%**, **12.8%** on the **HumanEval** dataset, **11.6%** on the **MBPP** dataset, and **12.44%** on the **BBH** dataset. The performance on all evaluations is shown in the table below.

![DEMO](./images/image.png)


## Evaluation Results

| Model             | MMLU  | C-Eval | GSM8K | MATH  | HumanEval | MBPP  | BBH   |
|-------------------|-------|--------|-------|-------|-----------|-------|-------|
| **Qwen1.5-7B-Chat**   | 60.88 | 70.18  | 54.13 | 7.96  | 31.10     | 15.00 | 31.67 |
| **Qwen-WisdomVast**   | 57.09 | **70.82**  | 51.93 | **13.12** | **43.90**     | **26.60** | **44.11** |


Explanation:

Since the official evaluation performance of Qwen1.5-7B-Chat has not been disclosed, we conducted our own testing using [opencompass](https://github.com/open-compass/opencompass) and obtained the above results.

Qwen-WisdomVast was tested using the same parameters as Qwen1.5-7B-Chat.


## Download Model

| Model             | Download  |
|:-------------------:|:-----------:|
| Qwen1.5-7B        |[ 🤗 HuggingFace](https://huggingface.co/Qwen/Qwen1.5-7B) [  🤖 ModelScope](https://modelscope.cn/models/qwen/Qwen1.5-7B)|
| Qwen-WisdomVast-Lora           |[ 🤗 HuggingFace](https://huggingface.co/zhichen/Qwen-WisdomVast-Lora) [  🤖 ModelScope](https://modelscope.cn/models/seanzhang/Qwen-WisdomVast-Lora)|
| Qwen-WisdomVast (Merged Model)           |[ 🤗 HuggingFace](https://huggingface.co/zhichen/Qwen-WisdomVast) [  🤖 ModelScope](https://modelscope.cn/models/seanzhang/Qwen-WisdomVast)|


## Merge LORA Model (Skippable)

1、Download [Qwen1.5-7B](https://modelscope.cn/models/qwen/Qwen1.5-7B)

```bash
git clone https://www.modelscope.cn/qwen/Qwen1.5-7B.git
```

2、Download [Qwen-WisdomVast-Lora](https://www.modelscope.cn/models/seanzhang/Qwen-WisdomVast-Lora)

**From ModelScope**
```bash
git lfs install
git clone https://www.modelscope.cn/seanzhang/Qwen-WisdomVast-Lora.git

```

**From HuggingFace**
```bash
git lfs install
git clone https://huggingface.co/zhichen/Qwen-WisdomVast-Lora
```

3、Merge Model

```bash
python merge_lora.py \
    --base_model path/to/qwen/Qwen1.5-7B \
    --lora_model path/to/lora/Qwen-WisdomVast-Lora \
    --output_dir ./Qwen-WisdomVast
```


## Download Qwen-WisdomVast (Merged Model)

**From ModelScope**
```bash
git lfs install
git clone https://www.modelscope.cn/seanzhang/Qwen-WisdomVast.git

```

**From HuggingFace**
```bash
git lfs install
git clone https://huggingface.co/zhichen/Qwen-WisdomVast
```

## CLI DEMO

```bash
python cli_demo.py  --model_path ./Qwen-WisdomVast(Replace it with your own merged model path)
```

## WEB DEMO

```bash
python web_demo.py  --model_path ./Qwen-WisdomVast(Replace it with your own merged model path)
```


## VLLM WEB DEMO

1、Use [vllm](https://github.com/vllm-project/vllm) deploy model

```bash
python -m vllm.entrypoints.openai.api_server --served-model-name Qwen-WisdomVast --model ./Qwen-WisdomVast(Replace it with your own merged model path)
```

2、This command is executed on the CLI

```bash
python vllm_web_demo.py --model Qwen-WisdomVast 
```


## Repeat the evaluation results

1、Use [vllm](https://github.com/vllm-project/vllm) deploy `openai api server`

deploy command:

```bash
python -m vllm.entrypoints.openai.api_server --served-model-name Qwen-WisdomVast --model ./Qwen-WisdomVast(Replace it with your own merged model path)
```

2、Use [opencompass](https://github.com/open-compass/opencompass) framework to eval

Reference: [Verify model effects using opencompass](https://blog.csdn.net/qq_44193969/article/details/134979054)

After modifying as described above, copy the `eval_qwen_wisdomvast.py` file in the `opencompass/configs` folder


3、Execute test script

```bash
python run.py configs/eval_qwen_wisdomvast.py  -w outputs/Qwen-WisdomVast
```


## LICENSE

This project can only be used for research purposes, and the project developer shall not bear any harm or loss caused by the use of this project (including but not limited to data, models, codes, etc.). For details, please refer to [DISCLAIMER](https://github.com/seanzhang-zhichen/Qwen-WisdomVast/blob/main/DISCLAIMER)。

The License agreement of the Qwen-WisdomVast project code is the [Apache License 2.0](./LICENSE). The code is free for commercial use, and the model weights and data can only be used for research purposes. Please attach a link to Qwen-WisdomVast and the licensing agreement in the product description.


## Citation

If you used Qwen-WisdomVast in your research, cite it in the following format:

```latex
@misc{Qwen-WisdomVast,
  title={Qwen-WisdomVast},
  author={Zhichen Zhang, Weihan Huang},
  year={2024},
  howpublished={\url{https://github.com/seanzhang-zhichen/Qwen-WisdomVast}},
}
```

## Acknowledgement

[QwenLM/Qwen1.5](https://github.com/QwenLM/Qwen1.5)
<br>
[hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
<br>
[shibing624/MedicalGPT](https://github.com/shibing624/MedicalGPT)
<br>
[modelscope/swift](https://github.com/modelscope/swift)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=seanzhang-zhichen/Qwen-WisdomVast&type=Date)](https://star-history.com/#seanzhang-zhichen/Qwen-WisdomVast&Date)