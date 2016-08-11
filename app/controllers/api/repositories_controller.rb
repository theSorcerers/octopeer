class Api::RepositoriesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:repository).permit(:owner, :name, :platform)
  end
end
