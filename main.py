import box
import timeit
import yaml
import argparse
from dotenv import find_dotenv, load_dotenv
from src.utils import setup_dbqa, setup_dbqa_basic
from src.llm import build_llm

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Import config vars
with open('config/config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('input',
    #                     type=str,
    #                     default='How much is the minimum guarantee payable by adidas?',
    #                     help='Enter the query to pass into the LLM')
    # args = parser.parse_args()

    # # Setup DBQA
    # start = timeit.default_timer()
    # dbqa = setup_dbqa()
    # response = dbqa({'query': args.input})
    # end = timeit.default_timer()

    # print(f'\nAnswer: {response["result"]}')
    # print('='*50)
    # print(f"Time to retrieve response: {end - start}")

    # # Process source documents
    # source_docs = response['source_documents']
    # for i, doc in enumerate(source_docs):
    #     print(f'\nSource Document {i+1}\n')
    #     print(f'Source Text: {doc.page_content}')
    #     print(f'Document Name: {doc.metadata["source"]}')
    #     print(f'Page Number: {doc.metadata["page"]}\n')
    #     print('='* 60)

    # print(f"Time to retrieve response: {end - start}")

    dbqa = build_llm()

    while True:
        question = input("\n\n--> What do you want to know? (Type 'exit' to quit): \n--> ")
        if question == "exit":
            break
        else:
            start = timeit.default_timer()
            response = dbqa(question)
            end = timeit.default_timer()

            print(f'\n<-- Answer: {response}')
            print('='*50)
            print(f"Time to retrieve response: {end - start}")

