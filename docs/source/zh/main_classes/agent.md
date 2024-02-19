<!--
Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

â ï¸ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# Agents API

<Tip warning={true}>

Transformers Agents is an experimental API that may change over time. Due to changes in the API or base models,
the output from agents may vary.

For more information about agents and tools, please refer to the [overview guide](../transformers_agents).
This page contains the API documentation for the base classes.

</Tip>

## Agents

We provide three types of agent classes: [`HfAgent`] uses open-source models for inference, [`LocalAgent`] uses models
provided by the user locally, and [`OpenAiAgent`] uses OpenAI's deployed models.

### HfAgent

[[autodoc]] HfAgent

### LocalAgent

[[autodoc]] LocalAgent

### OpenAiAgent

[[autodoc]] OpenAiAgent

### AzureOpenAiAgent

[[autodoc]] AzureOpenAiAgent

### Agent

[[autodoc]] Agent 
- chat 
- run 
- prepare_for_new_chat

## Tools

### load\_tool

[[autodoc]] load\_tool

### Tool

[[autodoc]] Tool

### PipelineTool

[[autodoc]] PipelineTool

### RemoteTool

[[autodoc]] RemoteTool

### launch\_gradio\_demo

[[autodoc]] launch\_gradio\_demo

## Agent Classes

Agents can handle objects of any class; tools are of various types and can accept and return text, images, audio,
video, etc. To add flexibility and ensure proper display of these objects in ipython (jupyter, colab, ipython
notebooks, etc.), we have implemented the following classes.

Objects of these classes should continue to operate as they did initially; text objects should continue to behave
as strings, and image objects should continue to behave as `PIL.Image` objects.

These classes have three specific purposes:

- When a class is called with `to_raw`, it should return a base-class object
- When a class is called with `to_string`, it should return the object as a string: in `AgentText`, it might be a
string, but in other contexts, it might be a list of paths for serialized objects
- When displayed in an ipython environment, the object should display correctly

### AgentText

[[autodoc]] transformers.tools.agent_types.AgentText

### AgentImage

[[autodoc]] transformers.tools.agent_types.AgentImage

### AgentAudio

[[autodoc]] transformers.tools.agent_types.AgentAudio
