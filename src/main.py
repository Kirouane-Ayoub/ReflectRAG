from graph.create_graph import app

while True:
    question = input(">>> ")
    inputs = {"question": question}

    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Finished running: {key}:")

    print(value["generation"])
