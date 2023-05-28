from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = "sqlite:///leaderboard.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class LeaderboardEntry(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    score = Column(Integer)

    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score


Base.metadata.create_all(engine)


class Leaderboard:
    def __init__(self):
        self.entries = []

    def add_score(self, player_name, score):
        if score is not None:
            entry = LeaderboardEntry(player_name=player_name, score=score)
            self.entries.append(entry)
            self.entries = sorted(self.entries, key=lambda x: x.score, reverse=True)[
                :15
            ]

    def save_leaderboard(self):
        for entry in self.entries:
            if entry.player_name and entry.score > 0:
                existing_entry = (
                    session.query(LeaderboardEntry)
                    .filter_by(player_name=entry.player_name)
                    .first()
                )

                if existing_entry:
                    existing_entry.score = entry.score
                else:
                    session.add(entry)
        session.commit()

    @staticmethod
    def load_leaderboard():
        leaderboard = Leaderboard()
        entries = (
            session.query(LeaderboardEntry)
            .order_by(LeaderboardEntry.score.desc())
            .limit(15)
            .all()
        )
        leaderboard.entries = entries
        leaderboard.scores = [
            {"player_name": entry.player_name, "score": entry.score}
            for entry in entries
        ]
        return leaderboard
