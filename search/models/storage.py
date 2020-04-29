from service import db


class Storage(db.Model):
    name = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    milvus_addr = db.Column(db.String(120), unique=False, nullable=False)
    milvus_port = db.Column(db.Integer, unique=False, nullable=False)
    milvus_table_name = db.Column(db.String(120), unique=False, nullable=False)
    milvus_dimension = db.Column(db.Integer, unique=False, nullable=False)
    milvus_index_file_size = db.Column(db.Integer, unique=False, nullable=False)
    milvus_metric_type = db.Column(db.String(120), unique=False, nullable=False)
    s3_addr = db.Column(db.String(120), unique=False, nullable=False)
    s3_port = db.Column(db.Integer, unique=False, nullable=False)
    s3_token = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Storage %r>' % self.name
