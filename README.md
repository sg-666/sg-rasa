# sg-rasa

After clone the repo, first if you don't have rasa already:
`pip3 install rasa`

Then
`rasa train`

Then open the rasa server
`rasa run --enable-api --cors "*"`

Whenever you have changes you want to reflect in frontend, which is sg, `rasa train`

### simple steps

1. define intent which is user input in nlu.yml
2. define response which is output to user in domain.yml
3. define the sequence in stories.yml
