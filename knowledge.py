import jinja2
import os 
from jinja2 import Template
import pandas as pd 
import re

latex_knowledgd_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = latex_knowledgd_env.get_template('knowledge.jinja2')

if __name__ == "__main__":

    df = pd.read_excel('knowledge_area_context_xlsx.xlsx')

    rows = df.to_dict(orient = 'records')
    goals = df['goal'].str.split(";")
    inputs = df['input'].str.split(";")
    activities = df['activity'].str.split(";")
    deliverables = df['deliverable'].str.split(";")
    suppliers = df['supplier'].str.split(";")
    participants = df['participant'].str.split(";")
    consumers = df['consumer'].str.split(";")
    techniques = df['technique'].str.split(";")
    tools = df['tool'].str.split(";")
    metrics = df['metric'].str.split(";")

    with open("knowledge.tex", "w") as f:
        f.write(template.render(
            rows = rows, 
            goals = goals,
            inputs = inputs,
            activities = activities,
            deliverables = deliverables, 
            suppliers = suppliers,
            participants = participants,
            consumers = consumers,
            techniques = techniques,
            tools = tools, 
            metrics = metrics
            ))