from mmengine.config import read_base
from opencompass.models import OpenAI
from opencompass.partitioners import NaivePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    # choose a list of datasets
    from .datasets.ceval.ceval_gen import ceval_datasets
    from .datasets.cmmlu.cmmlu_gen import cmmlu_datasets
    from .datasets.mmlu.mmlu_gen import mmlu_datasets
    from .datasets.gsm8k.gsm8k_gen import gsm8k_datasets
    from .datasets.bbh.bbh_gen import bbh_datasets
    from .datasets.math.math_gen import math_datasets
    from .datasets.mbpp.mbpp_gen import mbpp_datasets
    from .datasets.humaneval.humaneval_gen import humaneval_datasets

    # and output the results in a choosen format
    from .summarizers.medium import summarizer


datasets = [*ceval_datasets, *cmmlu_datasets, *mmlu_datasets, 
            *gsm8k_datasets, *bbh_datasets, *math_datasets, 
            *humaneval_datasets, *mbpp_datasets]


api_meta_template = dict(
    round=[
            dict(role='HUMAN', api_role='HUMAN'),
            dict(role='BOT', api_role='BOT', generate=True),
    ],
)

models = [
    dict(abbr='Qwen-WisdomVast',
        type=OpenAI, path='Qwen-WisdomVast',
        key='EMPTY',  # The key will be obtained from $OPENAI_API_KEY, but you can write down your key here as well
        meta_template=api_meta_template,
        query_per_second=10,
        max_out_len=2048, max_seq_len=4096, batch_size=8),
]

infer = dict(
    partitioner=dict(type=NaivePartitioner),
    runner=dict(
        type=LocalRunner,
        max_num_workers=8,
        task=dict(type=OpenICLInferTask)),
)
