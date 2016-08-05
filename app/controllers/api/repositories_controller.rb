class Api::RepositoriesController < ApplicationController
  before_action :set_repository, only: :show

  def index
    @repositories = Repository.all

    render json: @repositories
  end

  def show
    render json: @repository
  end

  def create
    @repository = Repository.new(repository_params)

    if @repository.save
      render json: @repository, status: :created
    else
      render json: @repository.errors, status: :unprocessable_entity
    end
  end

  private

  def set_repository
    @repository = Repository.find(params[:id])
  end

  def repository_params
    params.require(:repository).permit(:owner, :name, :platform)
  end
end
