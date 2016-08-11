class Api::SessionsController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:session).permit(:pull_request_id, :user_id)
  end
end
