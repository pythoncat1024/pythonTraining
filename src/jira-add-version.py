# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     jira-add-version
   Description :
   Author :       cat
   date：          2018/4/19
-------------------------------------------------
   Change Activity:
                   2018/4/19:
-------------------------------------------------
"""


def add_version():
    """
    create_version(name, project, description=None, releaseDate=None, startDate=None, archived=False, released=False)[source]
Create a version in a project and return a Resource for it.

        Parameters:
        name – name of the version to create
        project – key of the project to create the version in
        description – a description of the version
        releaseDate – the release date assigned to the version
        startDate – The start date for the version
    :return:
    """
    name, project, description, releaseDate, startDate, CIB_S_VARIANT = get_params()

    create_info = (name, project, description, releaseDate, startDate)
    print("add_version===args:::", create_info, CIB_S_VARIANT)
    if "userdebug".upper() != str(CIB_S_VARIANT).upper():
        import pprint
        from jira import JIRA

        jira = JIRA(r'http://192.168.59.239:8090', basic_auth=(r'gerrit', r'gerrit'))

        version = jira.create_version(*create_info)
        pprint.pprint(version)
    else:
        print("userdebug version can not add version to jira")


def _get_output_path(branch, variant, project):
    last_name = __get_name(project, branch, variant)
    return r"/home/build/release/dailybuild/{product}/{branch}/{last_name}".format(product=project,
                                                                                   branch=branch,
                                                                                   last_name=last_name)


def __get_name(project, branch, variant):
    """
    获取 daily 的路径名称 (最后一个文件名)
    :param project: tk_66_
    :param branch: gm12b
    :param variant: user/userdebug
    :return:
    """
    import os
    txt = os.path.join(r"/home/build/release", "_".join([project, branch, variant]) + ".txt")

    print(project, branch, variant)

    for line in open(txt):
        if len(line) > 0:
            return line.strip()


"""
# 使用datetime
timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
print otherStyleTime   # 2013--10--10 15:40:00

"""


def _get_daily_version_info(branch, variant, project):
    import os
    last_name = __get_name(project, branch, variant)
    path = r"/home/build/release/dailybuild/{product}/{branch}/{last_name}".format(product=project,
                                                                                   branch=branch,
                                                                                   last_name=last_name)
    prop_path = os.path.join(path, 'build.prop')
    nameKey = "ro.build.display.id="
    versionName = ""
    f = open(prop_path)
    for line in f:
        if line.startswith(nameKey):
            versionName = line[len(nameKey):].strip()
        if versionName:
            break
    f.close()
    versionTime = last_name[0:10]
    print(versionName, versionTime)
    return versionName, versionTime


def get_params():
    import sys
    args = sys.argv
    if len(args) < 5:
        raise Exception("params leak! please give me: [$product,$branch,$CIB_S_VARIANT,$JIRA_KEY_WORD]")
    print(args)
    product = args[1]
    branch = args[2]
    CIB_S_VARIANT = args[3]
    JIRA_KEY_WORD = args[4]
    # create_version(name, project, description=None, releaseDate=None, startDate=None, archived=False, released=False)
    name, timeStr = _get_daily_version_info(branch, CIB_S_VARIANT, product)
    project = JIRA_KEY_WORD
    description = ""
    releaseDate = timeStr
    startDate = timeStr

    return name, project, description, releaseDate, startDate, CIB_S_VARIANT


if "__main__" == __name__:
    add_version()
    pass
