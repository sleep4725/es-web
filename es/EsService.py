from elasticsearch import Elasticsearch

##
# @author JunHyeon.Kim
##
class EsService:

    @classmethod
    def get_cluster_health(cls, es_client: Elasticsearch)\
            -> bool:
        """
        :param es_client:
        :return:
        """
        response:dict= dict(es_client.cluster.health())
        status_code:str= response["status"]
        if status_code in ["yellow", "green"]:
            return True
        else:
            return False
