# How to Create a New Expert or Expand an Existing Expert

To create a new Domain Expert agent: 

1. Make a copy of [expert_template.py](../src/agents/experts/template/expert_template.py)
2. Name your new Domain Agent with the format `<domain>_expert.py` (example: the Buddhist Ethics Domain Expert is ethics_expert.py)
3. Update the constants in the new agent file.
4. Use [create_db_from_url.py](../src/agents/experts/utils/db_creation_scripts/create_db_from_url.py) to create a vector database for retrevial augmentation

To expand and existing Domain Expert agent:

1. Use [expand_db_from_url.py](../src/agents/experts/utils/db_creation_scripts/expand_db_from_url.py) to expand the vector database with your source

If these instructions are at all unclear, please alert me so that they can be updated. If you would like to create or expand an agent using a source that is not available as a web URL, (example: PDF, txt) a new creating script must be created.