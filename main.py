from absl import app
from absl import flags

import question_1
import question_2
from constants import dataset_dir

FLAGS = flags.FLAGS
flags.DEFINE_string("info",  "Unspecified", "This system manipulates data from the MASSIVE Dataset",)


def main(args):
    if FLAGS.question1:
        print(FLAGS.question1)
        question_1.process_all_files(dataset_dir)

    elif FLAGS.question2:
        # print(FLAGS.question2)
        question_2.partition_files()
        question_2.generate_translations()

    else:
        print("No options were specified")


if __name__ == '__main__':
    app.run(main)
