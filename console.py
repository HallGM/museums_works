import repositories.museum_repository as museum_repository
import repositories.work_repository as work_repository

# all_museums = museum_repository.select_all()
# for museum in all_museums:
#     print(museum.__dict__)

all_works = work_repository.select_all()
for work in all_works:
    print(work.title)