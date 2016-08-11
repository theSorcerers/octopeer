class Api::UsersController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:user).permit(:username)
  end
end
