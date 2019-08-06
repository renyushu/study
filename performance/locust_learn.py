from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {
            "username": "test",
            "password": "123456"
        })

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "https://debugtalk.com"
    min_wait = 1000
    
    max_wait = 5000

# 这个demo中表示，定于了针对 host 网站的测试场景：先模拟用户登录，然后随机地访问首页（/）和关于页面（/about/),
# 请求比列为1:2，并且，在测试过程中，两次请求的间隔时间为1—5的随机值

# 在locust的测试脚本中，所有的业务场景都是在Locust和TaskSet两个类的集成子类中进行描述的



"""



class HttpLocust(Locust)
    1, 在Locust类中有一个client属性，它对应着虚拟用户作为客户端所具备的请求能力，也就是我们说的请求方法，一般我们不会直接使用
        locust类，因为其client属性没有绑定任何方法。因此在使用Locust时，需要先继承Locust类，然后在继承子类中的client属性
        绑定客户端的实现类。
        
        Locust -- 
    
    
TaskSet
    放置需要测试的各种任务，这些任务用@task装饰器来标记
    


HttpLocust
    一个实例就代表了一个用户
        task_set成员需要引用TaskSet类
    
学习笔记：
    ab 不好控制
    

"""