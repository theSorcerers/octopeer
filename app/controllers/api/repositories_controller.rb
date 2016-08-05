class Api::RepositoriesController < ApplicationController
  def index
    render json: Repository.all
  end

  def show
    render json: Repository.find(params[:id])
  end

  def create
    repository = Repository.new(repository_params)
    if repository.save
      render json: repository
    else
      render json: { errors: repository.errors }
    end
  end

  private

  def repository_params
    params.require(:repository).permit(:owner, :name, :platform)
  end
end
