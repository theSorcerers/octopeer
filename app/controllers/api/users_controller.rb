class Api::UsersController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def user_params
    params.require(:user).permit(:username)
  end
end
