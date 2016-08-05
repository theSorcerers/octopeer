class Api::PullRequestsController < ApplicationController
  before_action :set_pull_request, only: :show

  def index
    @pull_requests = PullRequest.all

    render json: @pull_requests
  end

  def show
    render json: @pull_request
  end

  def create
    @pull_request = PullRequest.new(pull_request_params)

    if @pull_request.save
      render json: @pull_request, status: :created
    else
      render json: @pull_request.errors, status: :unprocessable_entity
    end
  end

  private

  def set_pull_request
    @pull_request = PullRequest.find(params[:id])
  end

  def pull_request_params
    params.require(:pull_request).permit(:repository_id, :pull_request_number)
  end
end
