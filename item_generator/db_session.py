import boto3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.engine.base import Engine


def get_engine() -> Engine:
    region = boto3.session.Session().region_name
    account_id = boto3.client('sts').get_caller_identity().get('Account')

    aurora_cluster_arn = f"arn:aws:rds:{region}:{account_id}:cluster:item-generator"
    secret_arn = f"arn:aws:secretsmanager:{region}:{account_id}:secret:items-generator-rds-credentials-vuEC7H"

    engine = create_engine('postgresql+auroradataapi://:@/items',
            echo=True,
            connect_args={
                "aurora_cluster_arn": aurora_cluster_arn,
                "secret_arn": secret_arn,
                "connect_timeout": 30,
            }
        )
    return engine


def get_session() -> Session:
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
