# Agent Engine Bug Minimal Example

I've been unable to successfully use an ADK Agent, deployed to Agent Engine. This is a minimal example highlighting the issue.

I've followed the the steps at https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart

First run:
```
pip install -r requirements.txt

```

The simple tool-using agent deploys successfully to Agent Engine:

```
python deploy-to-agent-engine.py
```

However, using the deployed agent results in an error. Calling `query` as is described in the Quick Start guide results in an error:

```
python query-agent.py
```

Resulting error:
```
<vertexai.agent_engines._agent_engines.AgentEngine object at 0x7fe1e8070100> 
resource name: projects/<GCLOUD PROJECT>/locations/us-central1/reasoningEngines/<DEPLOYED AGENT ID>
Traceback (most recent call last):
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/deploy-to-agent-engine.py", line 23, in <module>
    response = remote_agent.query(input={"messages": [
AttributeError: 'AgentEngine' object has no attribute 'query'
```

Trying to create a new session also results in an error:

```
python create-session.py
```

Resulting error:
```
Traceback (most recent call last):
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/google/api_core/grpc_helpers.py", line 76, in error_remapped_callable
    return callable_(*args, **kwargs)
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/grpc/_interceptor.py", line 277, in __call__
    response, ignored_call = self._with_call(
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/grpc/_interceptor.py", line 332, in _with_call
    return call.result(), call
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/grpc/_channel.py", line 440, in result
    raise self
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/grpc/_interceptor.py", line 315, in continuation
    response, call = self._thunk(new_method).with_call(
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/grpc/_channel.py", line 1198, in with_call
    return _end_unary_response_blocking(state, call, True, None)
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/grpc/_channel.py", line 1006, in _end_unary_response_blocking
    raise _InactiveRpcError(state)  # pytype: disable=not-instantiable
grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
        status = StatusCode.FAILED_PRECONDITION
        details = "Reasoning Engine Execution failed.
Please refer to our documentation (https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/troubleshooting/use) for checking logs and other troubleshooting tips.
Error Details: Service Unavailable"
        debug_error_string = "UNKNOWN:Error received from peer ipv4:172.217.169.74:443 {created_time:"2025-05-09T23:19:44.114104+01:00", grpc_status:9, grpc_message:"Reasoning Engine Execution failed.\nPlease refer to our documentation (https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/troubleshooting/use) for checking logs and other troubleshooting tips.\nError Details: Service Unavailable"}"
>

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/deploy-to-agent-engine.py", line 27, in <module>
    session = remote_agent.create_session(user_id="u_123")
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/vertexai/agent_engines/_agent_engines.py", line 1078, in _method
    response = self.execution_api_client.query_reasoning_engine(
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/google/cloud/aiplatform_v1/services/reasoning_engine_execution_service/client.py", line 863, in query_reasoning_engine
    response = rpc(
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__
    return wrapped_func(*args, **kwargs)
  File "/Users/keefmoon/SourceCode/agent-engine-bug-minimal-example/.venv/lib/python3.9/site-packages/google/api_core/grpc_helpers.py", line 78, in error_remapped_callable
    raise exceptions.from_grpc_error(exc) from exc
google.api_core.exceptions.FailedPrecondition: 400 Reasoning Engine Execution failed.
Please refer to our documentation (https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/troubleshooting/use) for checking logs and other troubleshooting tips.
Error Details: Service Unavailable
```

I've tried this in the following Google Cloud locations with the same results:
- `us-central1`
- `europe-west1`

I've also tried the equivalent REST command which also provide error responses.
