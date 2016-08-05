class Api::PullRequestsController < ApplicationController
  def index
    render json: PullRequest.all
  end

  def show
    render json: PullRequest.find(params[:id])
  end

  def create
    pull_request = PullRequest.new(pull_request_params)
    if pull_request.save
      render json: pull_request
    else
      render json: { errors: pull_request.errors }
    end
  end

  private

  def pull_request_params
    params.require(:pull_request).permit(:repository_id, :pull_request_number)
  end
end
