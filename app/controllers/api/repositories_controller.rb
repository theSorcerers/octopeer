class Api::RepositoriesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def repository_params
    params.require(:repository).permit(:owner, :name, :platform)
  end
end
