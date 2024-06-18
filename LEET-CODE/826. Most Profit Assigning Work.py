import collections


class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) :
        worker.sort()
        work_job=sorted(zip(difficulty,profit))
        current_profit,best_job,inedx=0,0,0
        for work in worker:
            while inedx < len(work_job) and work_job[inedx][0]<=work:
                best_job=max(best_job,work_job[inedx][1])
                inedx += 1
            current_profit+=best_job
        return current_profit
        # workJob=collections.namedtuple('workJob',['difficulty','profit'])
        # worker.sort()
        # work_queue=collections.deque(sorted(list(workJob(d,p) for d,p in zip(difficulty, profit)),key=lambda w:w[0]))
        # current_profit=0
        # best_job=0
        # for work in worker:
        #     while len(work_queue)>0 and work_queue[0].difficulty <= work :
        #         wj=work_queue.popleft()
        #         best_job=max(best_job,wj.profit)
        #     current_profit+=best_job
        # return current_profit
