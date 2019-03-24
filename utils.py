############################################################################################
#### INTRO RELATED

def main():
    # check if folders are created so I don't have to manually do it in a new import
    import os

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

# run main() when imported
main()
