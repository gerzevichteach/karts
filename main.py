import answers, images, problems
import title


def itog():
    return answers.t_answers('IV','4') + "\r\n" + \
           title.title('4') + "\r\n" + \
           problems.problems('IV','4')

if __name__ == '__main__':
    print(itog())


