import vertexai
from vertexai.preview import reasoning_engines
from multi_tool_agent import root_agent
from vertexai import agent_engines

PROJECT_ID = <Google Cloud Project ID>
LOCATION = "us-central1"
STAGING_BUCKET = <Bucket reference>

DEPLOYED_AGENT_ID = <Get deployed agent ID from running deploy-to-agent-engine.py>

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

remote_agent = agent_engines.get(DEPLOYED_AGENT_ID)
print(remote_agent)

response = remote_agent.query(input={"messages": [
    ("user", "What is weather in New York?")
]})
print(response)

# ```
# <vertexai.agent_engines._agent_engines.AgentEngine object at 0x7fe1e8070100> 
# resource name: projects/<GCLOUD PROJECT>/locations/us-central1/reasoningEngines/<DEPLOYED AGENT ID>
# Traceback (most recent call last):
#   File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/deploy-to-agent-engine.py", line 23, in <module>
#     response = remote_agent.query(input={"messages": [
# AttributeError: 'AgentEngine' object has no attribute 'query'
# ```
