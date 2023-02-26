from py2neo import Graph, Node, Relationship, NodeMatcher
from config import graph

with open(r"C:\Users\894\Desktop\毕业设计\KGQA_HLM-master\raw_data\relation_xiyouji.txt", encoding='utf-8') as f:
    for line in f.readlines():
        rela_array = line.strip("\n").split(",")
        print(rela_array)
        graph.run("MERGE(p: Person:Xiyouji{cate:'%s',Name: '%s'})" % (rela_array[3], rela_array[0]))
        graph.run("MERGE(p: Person:Xiyouji{cate:'%s',Name: '%s'})" % (rela_array[4], rela_array[1]))
        graph.run(
           "MATCH(e: Person), (cc: Person) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (rela_array[0], rela_array[1], rela_array[2], rela_array[2])

        )

        #graph.run("MATCH (p) WHERE p.cate='%s' AND p.Name= '%s' DETACH DELETE p" % (rela_array[3], rela_array[0]))
        #graph.run("MATCH (p) WHERE p.cate='%s' AND p.Name= '%s' DETACH DELETE p" % (rela_array[4], rela_array[1]))
