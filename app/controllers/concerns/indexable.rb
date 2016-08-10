module Indexable
  extend ActiveSupport::Concern

  def index
    @resources = controller_name.classify.constantize.all

    render json: @resources
  end
end
