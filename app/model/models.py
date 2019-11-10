from app.model import baseData, indexData, articalData, tutorialData, quiz
from app.database.dataManager import dataManager


def test_model():
    return "This is test Data"


def load_index_page_data():
    # Load index page data from database or somewhere else
    data = indexData.IndexData("课程列表")
    left_row = data.getLeftRow()
    raw_course_list = dataManager.getCourseList()
    # make raw db queue to the structure we need
    # get course list
    composite_list = []
    for instance in raw_course_list:
        # extract name and set url
        list_composite = baseData.ListComposite(instance.name)
        list_composite.setURL("tutorial/" + str(instance.id))
        composite_list.append(list_composite)
    left_row.setContent(composite_list)
    # Recent article
    raw_artical_list = dataManager.get_recent_article_list()
    article_list = []
    for instance in raw_artical_list:
        article = articalData.ArticalData(instance)
        article_list.append(article)
    data.setRecentArticalList(article_list)
    return data


def load_tutorial_course_page_data(course_id):
    # Load the course
    course = dataManager.get_course(course_id)
    if course is None:
        # Course code not found - 404
        pass
    # Load index page data from database or somewhere else
    data = tutorialData.TutorialData(course.name)
    left_row = data.getLeftRow()
    kv_mapping = {}
    raw_content_list = dataManager.get_course_class(course_id)
    for instance in raw_content_list:
        # print(instance)
        # (<app.database.dbClass.CourseContent object>, <app.database.dbClass.Artical object>)
        if instance[0].label in kv_mapping:
            kv_mapping[instance[0].label][instance[1].title] = instance
        else:
            kv_mapping[instance[0].label] = {}
            kv_mapping[instance[0].label][instance[1].title] = instance
    keyList = list(kv_mapping.keys())
    keyList.sort()
    # side bar
    composite_list = []
    # key: title  val: instance (tuple)
    for k in keyList:
        # parent layer
        parent = baseData.ListComposite(k)
        queuePairDir = kv_mapping[k]
        subKeyList = list(queuePairDir.keys())
        subKeyList.sort()
        for subKey in subKeyList:
            # child layer
            child = baseData.ListComposite(subKey)
            instanceTuple = queuePairDir[subKey]
            child.setURL('/artical/' + str(instanceTuple[1].id))
            child.setID(instanceTuple[1].id)
            parent.addChild(child)
        composite_list.append(parent)
    # set up side bar content
    data.getLeftRow().setContent(composite_list)
    return data


def load_article_data(article_id):
    article_db = dataManager.get_article(article_id)
    if article_db is None:
        return None
    return articalData.ArticalData(article_db)


def load_tutorial_article_data(course_id, article_id):
    data = load_tutorial_course_page_data(course_id)
    article = load_article_data(article_id)
    data.setArtical(article)
    return data


def load_quiz_data(article_id):
    article_db = dataManager.get_article(article_id)
    if article_db is None:
        return None
    data = quiz.QuizArticleData(article_db)
    mcq1 = quiz.QuestionMultipleChoice(0, "C语言中有一个常用函数叫做printf。", "printf返回的值是什么？")
    mcq1.add_choice(0, "返回True/False", "返回的是整型(int)", False)
    mcq1.add_choice(1, "读取成功时候返回1， 否则返回0", "返回的是读取变量的个数，出错返回-1", False)
    mcq1.add_choice(2, "读取变量的个数，如果出错返回一个负数", "这是正确答案", True)
    mcq1.add_choice(3, "我不知道", "NB", True)
    data.add_question(mcq1)
    tfq1 = quiz.QuestionTextfield(1, "C语言中printf，fprintf，sprintf都是常用的函数", "请解答下列问题")
    tfq1.add_textfield(0, "printf返回什么？", "提示：返回的类型是int", "见上一小题", "返回读取变量个数，失败返回-1", 'small')
    tfq1.add_textfield(1, "fprintf是什么", "提示：翻man", "cnm你不会百度？", "嘴子这么欠谁也保不了你", 'small')
    tfq1.add_textfield(2, "还有什么想问的吗？", "", "感谢回复", "用来测试大文本框", 'medium')
    tfq1.add_textfield(3, "这段代码错在哪？<code>while(){printf(\"%s\", 'text')}</code>", "", "感谢回复", "用来测试大文本框", 'medium')
    data.add_question(tfq1)
    # TODO: Handle database queue
    # questions_db = dataManager.get_questions(article_id)
    return data
