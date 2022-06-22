from fastapi import APIRouter, HTTPException
from controllers.TestController import TestResults as TestResultsClass
from models.TestModels import TestCreate, TestResults

router = APIRouter(
  prefix="/results",
  tags=["results"]
)

initResults = TestResultsClass()

@router.post("/", response_model=TestCreate)
async def post_test_results(testResults: TestResults):
  response = await initResults.create_test_results(testResults.dict())

  if response:
    return response
  raise HTTPException(400, "Something went wrong / Bad request")

@router.delete("/{id}")
async def delete_test_results_by_id(id):
  response = await initResults.remove_result(id)
  if response:
    return f"Succesfully deleted test results with id {id}"
  raise HTTPException(400, f"There is no test results with id {id}")