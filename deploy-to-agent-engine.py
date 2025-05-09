import vertexai
from vertexai.preview import reasoning_engines
from multi_tool_agent import root_agent
from vertexai import agent_engines

PROJECT_ID = <Google Cloud Project ID>
LOCATION = "us-central1"
STAGING_BUCKET = <Bucket reference>

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

deployments = agent_engines.list()
print("Deployments")
print(deployments)

remote_app = agent_engines.create(
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]"   
    ]
)

print("Deployed")
print(remote_app.resource_name)
