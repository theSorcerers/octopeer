class Api::PullRequestsController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def pull_request_params
    params.require(:pull_request).permit(:repository_id, :pull_request_number)
  end
end
