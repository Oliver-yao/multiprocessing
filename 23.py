import multiprocessing
from time import ctime


def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item == None:
            break
        print('pull ', item, ' out of q') #此处替换为有用的工作
        # input_q.task_done() #发出信号通知任务完成
        print("Out of consumer: ", ctime()) # 此句执行完成再转入主程序

def producer(sequence, output_q):
    print("Into producer", ctime())
    for item in sequence:
        output_q.put(item)
        print("Put ", item, " into q")
    print("Out of producer:",ctime())

# 建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
   # cons_p.daemon = True
    cons_p.start()

    # 生产多个项，sequence 代表要发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    # 等待所有项被处理
    # cons_p.join()